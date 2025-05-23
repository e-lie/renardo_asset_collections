sccode = """
SynthDef.new(\\zap,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8, room=0, verb=0|
var osc, env;
sus = sus * blur;
freq = In.kr(bus, 1);
freq = [freq, freq+fmod];
amp=(amp / 10);
osc=(Saw.ar(((freq * [1, 1.01]) + LFNoise2.ar(50).range(-2, 2))) + VarSaw.ar((freq + LFNoise2.ar(50).range(-2, 2)), 1));
env=EnvGen.ar(Env.perc(attackTime: 0.025,releaseTime: sus,level: amp,curve: -10), doneAction: 0);
osc=(osc * env);
osc = Mix(osc) * 0.5;
osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)}).add;

"""

synth = SCInstrument(
    shortname="zap",
    fullname="Zap",
    description="Zap synth",
    code=sccode,
    arguments={}
)
