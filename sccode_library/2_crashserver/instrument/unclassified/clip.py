sccode = """
SynthDef.new(\\clip, {
	|amp=1, sus=1, pan=0, freq=440, vib=0, fmod=0, rate=0, bus=0|
	var osc, env;
	freq = In.kr(bus, 1);
	freq = [freq, freq+fmod];
	osc = ClipNoise.ar();
	env = EnvGen.ar(Env.new([1, 1], [1, 1]), doneAction:1);
	osc = osc * env * amp;
	osc = Mix(osc) * 0.1;
	osc = Pan2.ar(osc , pan);
	ReplaceOut.ar(bus, osc)
	},
metadata: (
	credit: "CrashServer",
	modified_by: "",
	description: "",
	category: \\noise,
	tags: [\\tag]
	)
).add;
"""

synth = SCInstrument(
    shortname="clip",
    fullname="Clip",
    description="Clip synth",
    code=sccode,
    arguments={}
)
