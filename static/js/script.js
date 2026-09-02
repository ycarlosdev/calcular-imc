document.addEventListener('DOMContentLoaded', function(){
  const form = document.getElementById('imc-form');
  const result = document.getElementById('result');

  form.addEventListener('submit', async function(e){
    e.preventDefault();
    result.textContent = '';
    const weight = parseFloat(document.getElementById('weight').value);
    const height = parseFloat(document.getElementById('height').value);
    if(!weight || !height){
      result.textContent = 'Introduce peso y altura válidos.';
      return;
    }

    try{
      const res = await fetch('/calculate', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({weight, height})
      });
      const data = await res.json();
      if(res.ok){
        result.innerHTML = `<strong>IMC:</strong> ${data.imc} <br><strong>Clasificación:</strong> ${data.classification}`;
      } else {
        result.textContent = data.error || 'Error al calcular IMC';
      }
    }catch(err){
      result.textContent = 'Error de red';
    }
  });
});
