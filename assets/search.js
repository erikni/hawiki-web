const input=document.querySelector('#query');
if(input){
const normalize=s=>s.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
fetch('/search.json').then(r=>{if(!r.ok)throw Error();return r.json()}).then(items=>{
const render=()=>{const terms=normalize(input.value).trim().split(/\s+/).filter(Boolean);const found=items.filter(p=>terms.every(t=>normalize(p.title+' '+p.description).includes(t)));document.querySelector('#count').textContent=document.body.dataset.searchCount.replace('{count}',found.length);const root=document.querySelector('#results');root.replaceChildren();root.className='cards';found.forEach(p=>{const a=document.createElement('a');a.className='card';a.href='/'+p.slug+'/';const h=document.createElement('h3');h.textContent=p.title;const d=document.createElement('p');d.textContent=p.description;a.append(h,d);root.append(a)})};input.addEventListener('input',render);render();
}).catch(()=>{document.querySelector('#count').textContent=document.body.dataset.searchError;});}
