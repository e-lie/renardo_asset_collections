sccode = """
SynthDef.new(\\startSound,
{ arg bus, rate=1, sus; var osc;
	ReplaceOut.kr(bus, rate)}).add;

"""

effect = SCEffect(
    shortname="startsound",
    fullname="startSound",
    description="Startsound effect",
    code=sccode,
    arguments={},
    order=2,
)
