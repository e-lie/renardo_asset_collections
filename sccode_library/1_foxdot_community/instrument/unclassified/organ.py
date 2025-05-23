sccode = """
SynthDef.new(\\organ, {
	|f=440, width = 0.5, pan = 0.0, bus = 0, amp = 1, sus=1, freq=440, fmod=0, rate = 0.5|
	var signal, tapPhase, tap, tapPhaseL, tapPhaseR, tapL, tapR, comp1, comp2, comp3, comp4, comp5, comp6, output;
	var timeMod, eqMod, bufferL, bufferR, osc, env, input, theSine, oscs, scaler, lfo1, lfo2, lfo3, lfo4, lfo5, lfo6;
	env = EnvGen.ar(Env(times: [(sus * 0.25), (sus * 1)],levels: [0, amp, 0],curve: 'lin'), doneAction: 0);
	input = Vibrato.ar(VarSaw.ar(freq, 0, LFNoise2.kr(1)), 5, 0.1, 0, 0.2, 0.1, 0.7);
	theSine = SinOsc.ar(freq);
	oscs = 6;
	scaler = 1/oscs;
	lfo1 = LFTri.ar(fmod*1.51);
	lfo2 = LFTri.ar(fmod*1.11);
	lfo3 = LFTri.ar(fmod*1.31);
	lfo4 = LFTri.ar(fmod*0.71);
	lfo5 = LFTri.ar(fmod*0.61);
	lfo6 = LFTri.ar(fmod*0.51);
	comp1 = input > lfo1;
	comp2 = input > lfo2;
	comp3 = input > lfo3;
	comp4 = input > lfo4;
	comp5 = input > lfo5;
	comp6 = input > lfo6;
	output = scaler*(comp1+comp2+comp3+comp4+comp5+comp6);
	output = output+0.001*theSine;
	freq = In.kr(bus, 1);
	freq = [freq, freq+fmod];
	output = 0.01 * LeakDC.ar(output, 0.9995);
	output = MoogFF.ar(output.tanh*20.0, (f*12 ) + LFNoise2.ar(1, 400, 1), LFNoise2.ar(0,3.5, 0));
	output = MoogFF.ar(output*4, f*LFNoise2.kr(0.2, 6, 4), 0.5);

	timeMod = LFDNoise3.ar(rate, 0.0005);
    	eqMod = LFDNoise3.kr(1, 400);
	osc = 2*env*output.tanh;
	osc = Mix(osc) * 0.5;
	osc = HPF.ar(osc, 40);
	osc = LPF.ar(osc, 14000);
	osc = Splay.ar(osc * amp, pan);
	ReplaceOut.ar(bus, osc)
},
metadata: (
	credit: "Credit",
	modified_by: "Jens Meisner",
	decription: "Description",
	category: \\organ,
	tags: [\\keys, \\tag]
)).add;


"""

synth = SCInstrument(
    shortname="organ",
    fullname="Organ",
    description="Organ synth",
    code=sccode,
    arguments={}
)
