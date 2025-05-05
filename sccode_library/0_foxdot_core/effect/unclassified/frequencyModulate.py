sccode = """
SynthDef.new(\\frequencyModulate,
{|bus, fmod|
var osc;
osc = In.kr(bus, 1);
osc = [osc, osc+fmod];
ReplaceOut.kr(bus, osc)}).add;
"""

effect = SCEffect(
    shortname="frequencymodulate",
    fullname="frequencyModulate",
    description="Frequencymodulate effect",
    code=sccode,
    arguments={},
    order=2,
)
