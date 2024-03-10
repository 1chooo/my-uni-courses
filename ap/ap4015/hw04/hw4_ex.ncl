  lines  = asciiread("012400.txt",-1,"string")
  nlines = dimsizes(lines)
;  print(nlines)

  mlon  = 121 ;90~180 0.75
  nlat  = 61 ;15~60 0.75
  levs  = 5 ;300,500,700,850,1000
  vars  = 4 ;H,U,V,T
  var   = new ( (/vars,levs,nlat,mlon/), float)

  pressure_levels = (/ 300,500,700,850,1000 /)

  nl    = 0    ; line counter
  nvar = 0
  nlev = 0
  do while(nl.lt.nlines)
;---Read the first character of this line
    first = str_get_cols(lines(nl),0,0)
;---If it's a "%", then increment to next line.
    if(first.eq."D") then
      nl = nl + 1           ; increment line counter
      continue
    else
;---Otherwise, get the number of rows and read the data.
      nrows = 739 ;toint(lines(nl))
      if(nvar .gt. vars-1)then
         nvar = 0
         nlev = nlev + 1
      end if
      nl = nl + 1           ; increment line counter
      ;print("==================================================")
      ;print("Reading " + nrows + " rows of data.")
;
; Clean up the strings so there's only one space between
; each string, and no extra space at beginning or end.
; This allows us to use str_split_csv to parse this
; chunk of data. str_split_csv expects a single character
; delimiter (a space in this case).
;
      lines(nl:nl+nrows-1) = str_sub_str(lines(nl:nl+nrows-1),"    "," ")
      lines(nl:nl+nrows-1) = str_sub_str(lines(nl:nl+nrows-1),"   "," ")
      lines(nl:nl+nrows-1) = str_sub_str(lines(nl:nl+nrows-1),"  "," ")
      lines(nl:nl+nrows-1) = str_strip(lines(nl:nl+nrows-1))

;---Parse the data into a 2D integer array
      x = tofloat(str_split_csv(lines(nl:nl+nrows-1)," ",0))
      nl = nl + nrows

; . . .Do something here with 'x', like write it to a file. . .
      x1D =  ndtooned(x)
      ;print(x1D(0:121*61-1))
      ;print(nvar+" "+nlev)
      var(nvar,nlev,:,:) = reshape(x1D(0:mlon*nlat-1),(/nlat,mlon/))
      ;print(x1D(0)+"  "+x1D(mlon*nlat-1))   
      nvar = nvar + 1
    end if
  end do

lat = fspan(15,60,nlat)
lon = fspan(90,180,mlon)
H = var(0,:,:,:)
H!0="lev"
H!1="lat"
H!2="lon"
H&lat=lat
H&lon=lon
H&lat@units="degrees_north"
H&lon@units="degrees_east"
U = var(1,:,:,:)
V = var(2,:,:,:)
T = var(3,:,:,:)
copy_VarCoords(H,U)
copy_VarCoords(H,V)
copy_VarCoords(H,T)

do level = 0,levs-1
 wks = gsn_open_wks ("png", "hw4_"+pressure_levels(level)+"hPa")        ; send graphics to PNG file

 res                 = True                    ; plot mods desired
 res@gsnDraw         = False                   ; don't draw yet
 res@gsnFrame        = False                   ; don't advance frame yet
 res@gsnAddCyclic    = False

 mpres = res
 mpres@cnLevelSpacingF = 5
 mpres@tiMainOn        = False
 mpres@cnFillOn        = True                    ; turn on color 
 mpres@cnFillPalette   = "gui_default"           ; set color map
 mpres@cnLinesOn       = False                   ; turn off contour lines
 ;mpres@cnLineLabelsOn  = False                   ; tuen off line labels

 mpres@mpLimitMode     = "LatLon"     ; required
 mpres@mpMinLatF       =  15.         ; min lat
 mpres@mpMaxLatF       =  60.         ; max lat
 mpres@mpMinLonF       =  90.        ; min lon
 mpres@mpMaxLonF       = 180.        ; max lon
 
 plot = gsn_csm_contour_map(wks, T(level,:,:), mpres)

 zres = res
 zres@cnFillOn         = False
 ;zres@cnLineLabelPerimOn = False
 zres@cnLineLabelBackgroundColor = -1
 zres@cnInfoLabelOn    = False
 zres@lbLabelBarOn     = False                   ; will draw a panel label bar instead
 zres@cnLineColor      = "white"
 zres@cnLineThicknessF = 3.0
 if (pressure_levels(level) .le. 500)then
   zres@cnLevelSpacingF = 60
 else
   zres@cnLevelSpacingF = 30
 end if 

 plot2 = gsn_csm_contour(wks, H(level,:,:), zres)

 vecres = res
 vecres@vcGlyphStyle              = "WindBarb"     ; select wind barbs
 vecres@vcRefLengthF              = 0.008           ; define length of vec ref
 vecres@vcRefAnnoOn               = False          ; turn off ref wind barb
 vecres@vcMinDistanceF            = 0.012          ; thin out windbarbs
 vecres@vcWindBarbLineThicknessF  = 3.             ; set the wind barb thickness
 vecres@trYReverse                = True           ; reverse the Y-axis
 vecres@vcWindBarbColor           = (/111,111,111/)/255.

 vector = gsn_csm_vector(wks,U(level,:,:),V(level,:,:),vecres)
 
 overlay(plot,plot2)
 overlay(plot,vector)
 draw(plot)
 frame(wks)

end do
