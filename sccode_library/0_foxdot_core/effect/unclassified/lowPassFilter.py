sccode = """
SynthDef.new(\\lowPassFilter,
{|bus, lpf, lpr|
var osc;
osc = In.ar(bus, 2);
osc = RLPF.ar(osc, lpf, lpr);
ReplaceOut.ar(bus, osc)}).add;
"""

effect = SCEffect(
    shortname="lpf",
    fullname="lowPassFilter",
    description="Lowpassfilter effect",
    code=sccode,
    arguments={
        "lpf": 0,
        "lpr": 1
    },
    order=2,
)
