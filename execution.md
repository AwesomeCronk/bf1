### + (increment data)
- Data_Out; Changer_In
- Changer_Add
- Changer_Out; Data_In
- Counter_Cnt; Step_Rst

### - (decrement data)
- Data_Out; Changer_In
- Changer_Sub
- Changer_Out; Data_In
- Counter_Cnt; Step_Rst

### , (get input)
- Input_Await
- Input_Out; Data_In
- Counter_Cnt; Step_Rst

### . (set output)
- Data_Out; Output_In
- Counter_Cnt; Step_Rst

### < (decrement pointer)
- Pointer_Inc
- Counter_Cnt; Step_Rst

### > (increment pointer)
- Pointer_Dec
- Counter_Cnt; Step_Rst
  
### [ and ]
- Data_Out; if (not Seek) and ShouldTrigger then latch TargetDepth
- Data_Out; increment/decrement Depth (decrement if ((NOT ShouldTrigger) AND (`]` XOR Dir)))
- Data_Out; if ShouldTrigger then {set Seek; if `]` then set Dir}
- if Depth == TargetDepth then {reset Seek; reset Dir}
- if Dir then decrement Counter else increment Counter (use Seek to dictate Counter En so that seeking actually works)

### Notes
Data_Out must be active if checking ShouldTrigger.