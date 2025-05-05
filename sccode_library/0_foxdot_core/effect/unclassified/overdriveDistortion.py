sccode = """
SynthDef.new(\\overdriveDistortion,
{|bus, drive|
var osc;
osc = In.ar(bus, 2);
osc = (osc * (drive * 50)).clip(0,0.2).fold2(2);
ReplaceOut.ar(bus, osc)}).add;
"""

effect = SCEffect(
    shortname="drive",
    fullname="overdriveDistortion",
    description="Overdrivedistortion effect",
    code=sccode,
    arguments={
        "drive": 0
    },
    order=2,
)
