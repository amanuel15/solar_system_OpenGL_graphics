#version 330 core


layout (location = 0) in vec3 position;

layout (location = 1) in vec3 color;

layout (location = 2) in vec2 texCoord;



out vec3 newColor;

out vec2 outTexCoord;


uniform vec3 newPos = vec3(0, 0, 0);
uniform vec3 newVec = vec3(0, 0, 0);
uniform mat4 transform;



mat4 rotate(vec3 angle){
	mat4 x = mat4(
		1,	0,	0,	0,
		0,cos(angle[0]),-sin(angle[0]),0,
		0,sin(angle[0]),cos(angle[0]),0,
		0,	0,	0,	1
		);

	mat4 y = mat4(
		cos(angle[1]),0,sin(angle[1]),0,
		0,	1,	0,	0,
		-sin(angle[1]),0,cos(angle[1]),0,
		0,	0,	0,	1
		);

	mat4 z = mat4(
		cos(angle[2]),-sin(angle[2]),0,0,
		sin(angle[2]),cos(angle[2]),0,0,
		0,	0,	1,	0,
		0,	0,	0,	1
		);
	return transpose(x)*transpose(y)*transpose(z);	
}

mat4 translate(vec3 move){
	mat4 m = mat4(
		1,0,0, move[0],
		0,1,0, move[1],
		0,0,1, move[2],
		0,0,0,1
	);
	return transpose(m);
}


void main()
{

	vec3 x = newVec;
	vec3 m = newPos;    
	vec4 p = vec4(position, 1.0);
	p = translate(m) * p * rotate(x);
	gl_Position = p;		
    
	outTexCoord = vec2(texCoord.x, 1.0 - texCoord.y);
	newColor = color;
}
