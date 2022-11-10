### + (increment data)
- Data_Out; Changer_In
- Changer_Add
- Changer_Out; Data_In
- Counter_Inc

### - (decrement data)
- Data_Out; Changer_In
- Changer_Sub
- Changer_Out; Data_In
- Counter_Inc

### , (get input)
- Input_Await
- Input_Out; Data_In
- Counter_Inc; Step_Reset
- 

### . (set output)
- Data_Out; Output_In
- Counter_Inc; Step_Reset
- 
- 

### < (decrement pointer)
- Pointer_Inc
- Counter_Inc; Step_Reset
- 
- 

### > (increment pointer)
- Pointer_Dec
- Counter_Inc; Step_Reset
- 
- 

### [ and ]
- if not (Seek and ShouldTrigger) then latch TargetDepth
- increment/decrement CurrentDepth (inverse if Dir); if ShouldTrigger then {set Seek; if `]` then set Dir}
- if CurrentDepth == TargetDepth then {reset Seek; reset Dir}
- if Seek and Dir then decrement Counter else increment Counter
