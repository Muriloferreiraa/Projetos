const hora = 50
if(hora >=0 && hora <=11 ){
console.log('bom dia')
} 
else if(hora >=12 && hora <= 17){
    console.log('boa tarde')
}
 else if(hora >=18 && hora <=23){
  console.log('boa noite')
}
else{
    console.log('não encontrado')
}


//  const numero = Number(prompt('Digite um número:'));
//  const numeroTitulo = document.getElementById('numero-titulo');
//   const texto = document.getElementById('texto');

//  numeroTitulo.innerHTML = numero;
//   texto.innerHTML = '';
//   texto.innerHTML += `<p>Raiz quadrada : ${numero ** 0.5}.</p>`;
//   texto.innerHTML += `<p>${numero}é inteiro: ${Number.isInteger(numero)}</p>`;
//  texto.innerHTML += `<p>É NaN: ${Number.isNaN(numero)}.</p>`;
//   texto.innerHTML += `<p>Arredondando para baixo: ${Math.floor(numero)}</p>`;
//  texto.innerHTML += `<p>Arredondando para cima: ${Math.ceil(numero)}</p>`;
//  texto.innerHTML += `<p>Casas decimais: ${numero.toFixed(2)}</p>`;