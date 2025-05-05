sccode = """
SynthDef.new(\\fxout, {
	|bus, fx1, lpfx1, hpfx1|
	var osc,fxsig;
	osc = In.ar(bus, 2);
	fxsig = LPF.ar(osc, lpfx1);
	fxsig = HPF.ar(fxsig, hpfx1);
	Out.ar(2, Mix.ar(fxsig*fx1));
	ReplaceOut.ar(bus, osc)
}).add;
"""

effect = SCEffect(
    shortname="fx1",
    fullname="fxout",
    description="Fxout effect",
    code=sccode,
    arguments={
        "fx1": 0,
        "lpfx1": 22000,
        "hpfx1": 0
    },
    order=2,
)
