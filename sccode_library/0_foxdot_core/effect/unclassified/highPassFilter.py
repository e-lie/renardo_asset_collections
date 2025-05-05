sccode = """
SynthDef.new(\\highPassFilter,
{|bus, hpf, hpr|
var osc;
osc = In.ar(bus, 2);
osc = RHPF.ar(osc, hpf, hpr);
ReplaceOut.ar(bus, osc)}).add;
"""

effect = SCEffect(
    shortname="hpf",
    fullname="highPassFilter",
    description="Highpassfilter effect",
    code=sccode,
    arguments={
        "hpf": 0,
        "hpr": 1
    },
    order=2,
)
