sccode = """
SynthDef.new(\\gaze, {
	|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, blur=1, beat_dur=1, atk=0.0001, decay=0.01, rel=0.01, peak=1, level=0.8, wave=0, freq1=880, freq2=880, res1=0.0, res2=0.0, rate1=10, rate2 = 10, rate3 = 10, depth1=1, depth2=1, depth3=1, lfo1=0, lfo2=0, lfo3 = 0|
	var sig, env, detuned, pitch, lfo1wave, lfo2wave, lfo3wave, filter1;

		~wt = Array.fill(90, {
			var numSegs = rrand (90, 20);
			Env(
				(({rrand(0.0, 1.0)}!(numSegs-1))*[1, -1]).scramble,
				{rrand(1, 20)}!numSegs,
				'sine'
				// {rrand(-20,20)}!numSegs
			).asSignal(1024).asWavetable;
		});
		~vbuf = Buffer.allocConsecutive(90, s, 2048);
		~vbuf.do({
			arg buf, i;
			buf.loadCollection(~wt[i]);

		});

	sus = sus * blur;
	freq = In.kr(bus, 1);
	lfo1wave=Select.kr(lfo1, [LFTri.kr(rate1), LFSaw.kr(rate1), LFPulse.kr(rate1)]);
	lfo2wave=Select.kr(lfo2, [LFTri.kr(rate2), LFSaw.kr(rate2), LFPulse.kr(rate2)]);
	lfo3wave=Select.kr(lfo3, [LFTri.kr(rate3), LFSaw.kr(rate3), LFPulse.kr(rate3)]);
	detuned = VOsc.ar(wave, freq+fmod);

	wave = ~vbuf[0].bufnum + wave;
	env=EnvGen.ar(Env([0, peak, level, level, 0], [atk, decay, max((atk + decay + rel), sus - (atk + decay + rel)), rel], curve:\\sin), doneAction: 0);
	sig = VOsc.ar(wave, freq);
	sig = XFade2.ar(sig, detuned, 0.5);
	sig = MoogLadder.ar(sig, freq1*lfo1.range(1, depth1), res1);
	//sig = Decimator.ar(filter1, alias, redux);
	sig = MoogLadder.ar(sig, freq2*lfo2.range(1, depth2), res2);
	sig = Splay.ar(sig);
	sig = LeakDC.ar(sig);
	sig=sig*amp*env*lfo3.range(1, depth3);
	sig = Limiter.ar(sig, 0.9);

	ReplaceOut.ar(bus, sig)
},
metadata: (
	credit: "CrashServer",
	modified_by: "Jens Meisner",
	description: "",
	category: \\organ,
	tags: [\\tag]
	)
).add;
"""

synth = SCInstrument(
    shortname="gaze",
    fullname="Gaze",
    description="Gaze synth",
    code=sccode,
    arguments={}
)
