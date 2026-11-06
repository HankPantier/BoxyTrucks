// Show Us Your Rig form handler (Hank, Nov 5, 2026). Receives the multipart form from
// boxytrucks.com/submit/ and emails it, with photos attached, through Resend.
// Env vars (set in Vercel, never in the repo): RESEND_API_KEY (required),
// RIG_TO (default boxytrucks@gmail.com), RIG_FROM (default Resend's test sender).
const ALLOWED = ['https://boxytrucks.com', 'https://www.boxytrucks.com'];
const MAX_PHOTOS = 10;
const LABELS = {
  name: 'Name', email: 'Email', location: 'Based in', instagram: 'Instagram', youtube: 'YouTube',
  family: 'Family', generation: 'Generation', year: 'Year', nickname: 'Name of the truck',
  drivetrain: 'Engine & drivetrain', suspension: 'Suspension & lift', tires: 'Wheels & tires',
  armor: 'Armor & bumpers', storage: 'Racks, storage & sleeping', builders: 'Shops / builders',
  story: 'Story', best_trip: 'Best trip', full_res_photo_link: 'Full-res photo link',
  owns_photos: 'Owns photos', usage_ok: 'OK to publish', contact_ok: 'OK to contact for interview',
};

function cors(origin) {
  return {
    'Access-Control-Allow-Origin': ALLOWED.includes(origin) ? origin : ALLOWED[0],
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Vary': 'Origin',
  };
}
const json = (body, status, origin) =>
  new Response(JSON.stringify(body), { status, headers: { 'Content-Type': 'application/json', ...cors(origin) } });
const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

export function OPTIONS(request) {
  return new Response(null, { status: 204, headers: cors(request.headers.get('origin')) });
}

export async function POST(request) {
  const origin = request.headers.get('origin');
  if (origin && !ALLOWED.includes(origin)) return json({ ok: false, error: 'origin' }, 403, origin);
  if (!process.env.RESEND_API_KEY) return json({ ok: false, error: 'not configured' }, 500, origin);

  let form;
  try { form = await request.formData(); } catch { return json({ ok: false, error: 'bad form' }, 400, origin); }
  if (form.get('_honey')) return json({ ok: true }, 200, origin); // bots fill the hidden field; pretend success

  const v = (k) => String(form.get(k) || '').trim().slice(0, 5000);
  const email = v('email');
  if (!v('name') || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email) || !v('family') || !v('story'))
    return json({ ok: false, error: 'missing fields' }, 400, origin);

  const attachments = [];
  for (let i = 1; i <= MAX_PHOTOS; i++) {
    const f = form.get(`photo_${i}`);
    if (f && typeof f === 'object' && f.size > 0 && /^image\//.test(f.type || 'image/')) {
      const buf = Buffer.from(await f.arrayBuffer());
      attachments.push({ filename: (f.name || `photo-${i}.jpg`).replace(/[^\w.\- ]/g, '_'), content: buf.toString('base64') });
    }
  }

  const rows = Object.keys(LABELS).filter((k) => v(k))
    .map((k) => `<tr><th align="left" valign="top" style="padding:6px 12px 6px 0;color:#555">${LABELS[k]}</th><td style="padding:6px 0">${esc(v(k)).replace(/\n/g, '<br>')}</td></tr>`).join('');
  const subject = (v('_subject') || `New rig: ${v('year')} ${v('family')} — ${v('name')}`).slice(0, 200);
  const html = `<div style="font-family:system-ui,sans-serif;font-size:15px"><p><strong>New Show Us Your Rig submission</strong> · ${attachments.length} photo${attachments.length === 1 ? '' : 's'} attached. Reply to this email to answer ${esc(v('name'))}.</p><table>${rows}</table></div>`;

  const r = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: { Authorization: `Bearer ${process.env.RESEND_API_KEY}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      from: process.env.RIG_FROM || 'BoxyTrucks Rigs <onboarding@resend.dev>',
      to: [process.env.RIG_TO || 'boxytrucks@gmail.com'],
      reply_to: email,
      subject,
      html,
      attachments,
    }),
  });
  if (!r.ok) {
    console.error('resend', r.status, await r.text());
    return json({ ok: false, error: 'send failed' }, 502, origin);
  }
  return json({ ok: true, photos: attachments.length }, 200, origin);
}
