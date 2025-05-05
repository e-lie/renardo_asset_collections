sccode = """
SynthDef.new(\\SLPF,
{|bus, spf, spr, spfslide, spfend|
var osc,spfenv;
osc = In.ar(bus, 2);
spfenv = EnvGen.ar(Env.new([spf, spfend], [spfslide]));
osc = RLPF.ar(osc, spfenv, spr);
ReplaceOut.ar(bus, osc)}).add;
"""

effect = SCEffect(
    shortname="spf",
    fullname="SLPF",
    description="Slpf effect",
    code=sccode,
    arguments={
        "spf": 0,
        "spr": 1,
        "spfslide": 1,
        "spfend": 15000
    },
    order=2,
)
