const fs = require('fs');

const js = fs.readFileSync('routes.js', 'utf8');
const start = js.indexOf('qt=[');
const end = js.indexOf('];', start);
const arrayCode = js.slice(start + 3, end + 1);

// evaluate arrayCode in a safe scope
const months = eval(arrayCode);

const cleanMonths = months.map(m => {
  let img = typeof m.image === 'string' ? m.image : (m.image && m.image.url ? m.image.url : '');
  if (img.startsWith('/')) img = '.' + img;
  return {
    name: m.name,
    tagline: m.tagline,
    description: m.description,
    range: m.range,
    examples: m.examples,
    image: img,
    dot: m.dot
  };
});

fs.writeFileSync('clean_months.json', JSON.stringify(cleanMonths, null, 2), 'utf8');
console.log('Clean months written successfully! Count:', cleanMonths.length);
