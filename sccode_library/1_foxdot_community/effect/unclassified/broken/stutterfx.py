sccode = """
SynthDef.new(\\stutterfx, {
	|bus, t_reset, stut, stutrate, stutlen|
	var osc,dry,reset,wet;
	osc = In.ar(bus, 2);
	~stutter = { |snd, reset, stutlen, maxdelay = 1| var phase, fragment, del; phase = Sweep.ar(reset); fragment = { |ph| (ph - Delay1.ar(ph)) < 0 + Impulse.ar(0) }.value(phase / stutlen % 1); del = Latch.ar(phase, fragment) + ((stutlen - Sweep.ar(fragment)) * (stutrate - 1)); DelayC.ar(snd, maxdelay, del); };
	dry = osc;
	reset = Onsets.kr(FFT(LocalBuf(1024), osc), t_reset);
	wet = ~stutter.(osc, reset, stutlen);
	osc = SelectX.ar(stut, [dry, wet], wrap:1);
	ReplaceOut.ar(bus, osc)
}).add;
"""

effect = SCEffect(
    shortname="stut",
    fullname="stutterfx",
    description="Stutterfx effect",
    code=sccode,
    arguments={
        "t_reset": 0,
        "stut": 1,
        "stutrate": 1,
        "stutlen": 0.02
    },
    order=2,
)
