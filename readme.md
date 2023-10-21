There is a code for making a semantic term and testing input data.

each part is divided by regions.

example:
make a semantic term for: ```begin I := 1 ; R := 3 ; while X > I do begin R := R * 3 ; I := I + 1 ; end end```

output: ```AS_I(1) dot AS_R(3) dot WH(S2(gr, X =>, I =>), AS_R(S2(mult, R =>, 3_hat)) dot AS_I(S2(add, I =>, 1_hat)))```

testing is not completely full, it was made just for specific homework, will do the rest shortly.