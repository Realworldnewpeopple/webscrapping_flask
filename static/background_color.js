
//Create div element
//var cls = document.getElementById('image_info');
var cls=document.body;
//Give a height to div
//cls.style.height = '100vw';

//Append div to document
//document.body.appendChild(cls);

//Add event listener so document can listen to mouse movements
cls.addEventListener('mousemove', function(event) {

var x = event.clientX,
y = event.clientY;

cls.style.backgroundColor = 'rgb('+ x +', '+y+', +100)'
} );




