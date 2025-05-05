sccode = """
SynthDef.new(\\filterSwell,
{|bus, swell, sus, hpr|
var osc,env;
osc = In.ar(bus, 2);
env = EnvGen.kr(Env([0,1,0], times:[(sus*0.25), (sus*0.25)], curve:\\sin));
osc = RHPF.ar(osc, env * swell * 2000, hpr);
ReplaceOut.ar(bus, osc)}).add;
"""

effect = SCEffect(
    shortname="swell",
    fullname="filterSwell",
    description="Filterswell effect",
    code=sccode,
    arguments={
        "swell": 0,
        "sus": 1,
        "hpr": 1
    },
    order=2,
)
