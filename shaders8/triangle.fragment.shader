#version 330 core
in vec3 newColor;
in vec2 outTexCoord;
in vec2 outTexCoord2;
out vec4 outColor;
uniform sampler2D texSampler;
uniform vec3 fakeLighting;
uniform sampler2D texSampler2;
uniform vec3 mixe = vec3(0,0,0);
void main()
{
vec3 x = mixe;
outColor = vec4(newColor, 1.0);
vec3 fakeLighting = fakeLighting;
outColor = mix(texture(texSampler, outTexCoord),texture(texSampler2,outTexCoord),x[0])*vec4(fakeLighting[0],fakeLighting[1],fakeLighting[2], 1.0);
}