//Javascript to handle grid creation/drawing
//using p5

var cols = 9;
var rows = 9;

//COLORS
var WHITE = [255, 255, 255];
	BLACK = [0, 0, 0];
	GREEN = [0, 255, 0];
	RED  = [255, 0, 0];
	BLUE = [0,0,255];
	PURPLE = [142,68,173];
	ORANGE = [230,126,34];
    YELLOW = [255,255,0];
	TURQUOISE = [52, 231, 228];
// END OF COLORS

var colors = [WHITE,BLACK,GREEN,RED,BLUE,PURPLE,ORANGE,YELLOW,TURQUOISE];
var active_color = 1;
var active_size = 1;
var grid = [];
var colors_arr = document.getElementsByClassName('colors-box');

var size_arr = document.getElementsByClassName('size-box');
//var clearElem = document.getElementById("clear");



function setup(){
	var canvas = createCanvas(451,451);
	
	//Adding all Event Listeners

	for (let i = 0; i < colors_arr.length; i++) {
    	colors_arr[i].addEventListener('click', changeColor);
	}

	for (let i = 0; i < size_arr.length; i++) {
    	size_arr[i].addEventListener('click', changeSize);
	}
	
//	clearElem.addEventListener('click', clearAll);

	///////

	canvas.parent('sketch-holder');
	canvas.id('grid');


	for (let i = 0; i < rows; i++) {
		grid[i] = []
    	for (let j = 0; j < cols; j++) {
      		grid[i][j] = new Cell(i*50, j*50,50,50, 0);
	    }
	  }
}

function draw(){
	background(0);
	for (let i = 0; i < rows; i++) {
		for (let j = 0; j < cols; j++) {
      		grid[i][j].display();
      	}
	}
}

function mousePressed(event) {
	for (let i = 0; i < rows; i++) {
		for (let j = 0; j < cols; j++) {
		  	grid[i][j].clicked(mouseX,mouseY);
		}
	}
}

function mouseDragged(event) {
	for (let i = 0; i < rows; i++) {
		for (let j = 0; j < cols; j++) {
		  	grid[i][j].clicked(mouseX,mouseY);
		}
	}
}

function clearAll(){
	for (let i = 0; i < rows; i++) {
		for (let j = 0; j < cols; j++) {
		  	grid[i][j].color = colors[0];
		}
	}
}


var changeSize = function(){
	switch(this.htmlFor){
		case "option-sm":
			active_size = 1;
			break;
		case "option-md":
			active_size = 2;
			break;
		case "option-lg":
			active_size = 3;
			break;
		default:
			break;
	}
}


var changeColor = function() {
	switch(this.htmlFor){
		case "option1":
			active_color = 1;
			break;
		case "option2":
			active_color = 2;
			break;
		case "option3":
			active_color = 3;
			break;
		case "option4":
			active_color = 4;
			break;
		case "option5":
			active_color = 5;
			break;
		case "option6":
			active_color = 6;
			break;
		case "option7":
			active_color = 7;
			break;
		case "option8":
			active_color = 8;
			break;
		case "option9":
			active_color = 0;
		default:
			break;
	};
};


// A Cell object
class Cell {
  // Cell Constructor
  constructor(tempX, tempY, tempW, tempH, tempC) {
    this.x = tempX;
    this.y = tempY;
    this.w = tempW;
    this.h = tempH;
    this.color = colors[tempC];
  } 

  clicked(x, y){
  	let d = dist(x, y, this.x + this.w/2, this.y + this.h/2);
  	if(d < this.w * active_size / 2 ){
		this.setColorToActive(); 
	}
  }

   setColorToActive(){
  	this.color = colors[active_color];

  }
  

   display() {
    stroke(0);
    fill(this.color);
	rect(this.x,this.y,this.w,this.h);
  	}
}




