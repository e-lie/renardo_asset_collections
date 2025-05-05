sccode = """
SynthDef.new(\\ring_modulation,
{|bus, ring, ringl, ringh|
var osc,mod;
osc = In.kr(bus, 1);
mod = ring * SinOsc.ar(Clip.kr(XLine.kr(ringl, ringl + ringh), 20, 20000));
osc = ring1(osc, mod);
ReplaceOut.kr(bus, osc)}).add;
"""

effect = SCEffect(
    shortname="ring",
    fullname="ring_modulation",
    description="Ring_modulation effect",
    code=sccode,
    arguments={
        "ring": 0,
        "ringl": 500,
        "ringh": 1500
    },
    order=0,
)
