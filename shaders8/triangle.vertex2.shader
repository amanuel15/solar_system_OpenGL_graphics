#version 330 core
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 color;
layout (location = 2) in vec2 texCoord;
out vec3 newColor;
out vec2 outTexCoord;
out vec2 outTexCoord2;


uniform vec4 projection = vec4(0,0,0,0);
uniform vec3 newPos = vec3(0, 0, 0);
uniform vec3 newVec = vec3(0, 0, 0);
uniform vec3 celestialPos = vec3(0, 0, 0);
uniform vec3 celestialRot = vec3(0, 0, 0);
uniform mat4 transform;
uniform vec3 scale = vec3(1,1,1);

mat4 scaler(vec3 scale){
	mat4 m = mat4(
		scale[0],	0,	0,	0,
		0,	scale[1],	0,	0,
		0,	0,	scale[2],	0,
		0,	0,		0,		1
	);
	return transpose(m);


}

mat4 projector(vec4 project){
	float s = 1.0/tan(radians(project[0])/2.0);
	float sx = s/project[1];
	float sy = s;
	float zz = (project[3]+project[2])/(project[2]-project[3]);
	float zw = 2*project[3]*project[2]/(project[2]-project[3]);
	mat4 m = mat4(
		sx,  0,  0,  0,
		0,  sy,  0,  0,
		0,  0,  zz,  zw,
		0,  0,  -1,  0
		);

	return transpose(m);
}

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
	return transpose(z)*transpose(y)*transpose(x);	
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
{	vec4 f = projection;
	vec3 x = newVec;vec3 m = newPos;vec3 sc = scale;
	vec3 celestialPos = celestialPos;vec3 celestialRot = celestialRot;    
	vec4 p = vec4(position, 1.0);
	vec4 d =rotate(celestialRot)*translate(celestialPos)*translate(m)* scaler(sc)*rotate(x)*vec4(position, 1.0);
	gl_Position = projector(f) * d;
	outTexCoord = vec2(texCoord.x, 1.0 - texCoord.y);
	outTexCoord2 = vec2(texCoord.x,1.0 - texCoord.y);
	newColor = color;
}
