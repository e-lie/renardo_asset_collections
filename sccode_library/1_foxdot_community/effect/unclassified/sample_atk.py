sccode = """
SynthDef.new(\\sample_atk,
{|bus, sample_atk, sample_sus|
var osc,env;
osc = In.ar(bus, 2);
env = EnvGen.ar(Env.new(levels: [0,1,0], times:[sample_atk, sample_sus], curve: 'lin'));
osc = osc*env;
ReplaceOut.ar(bus, osc)}).add;
"""

effect = SCEffect(
    shortname="sample_atk",
    fullname="sample_atk",
    description="Sample_atk effect",
    code=sccode,
    arguments={
        "sample_atk": 0,
        "sample_sus": 1
    },
    order=2,
)
