await new Promise(r=>setTimeout(r,3500));
const b=[...document.querySelectorAll('button,div[role=button],a')].find(x=>/^View insights$/.test((x.innerText||'').trim()));
if(!b){ 'NOBUTTON '+location.pathname } else {
  b.click(); await new Promise(r=>setTimeout(r,4000));
  const t=(document.querySelector('[role=dialog]')||document.body).innerText;
  const g=(k)=>{const m=t.match(new RegExp('\\n'+k+'\\n([\\d,.]+%?)'));return m?m[1]:'';};
  JSON.stringify({p:location.pathname, views:g('Views'), viewers:g('Viewers'), interactions:g('Interactions'), likes:g('Likes'), comments:g('Comments'), saves:g('Saves'), shares:g('Shares'), visits:g('Profile visits'), taps:g('External link taps'), follows:g('Follows'), nonfollow:(t.match(/Non-followers\n([\d.]+%)/)||[])[1]||''});
}
