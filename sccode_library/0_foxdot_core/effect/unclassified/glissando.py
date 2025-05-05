sccode = """
SynthDef.new(\\glissando,
{|bus, glide, glidedelay, sus|
var osc;
osc = In.kr(bus, 1);
osc = osc * EnvGen.ar(Env([1, 1, (1.059463**glide)], [sus*glidedelay, sus*(1-glidedelay)]));
ReplaceOut.kr(bus, osc)}).add;
"""

effect = SCEffect(
    shortname="glide",
    fullname="glissando",
    description="Glissando effect",
    code=sccode,
    arguments={
        "glide": 0,
        "glidedelay": 0.5,
        "sus": 1
    },
    order=0,
)
