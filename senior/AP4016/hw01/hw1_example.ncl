  
  diri  = "./"                            ; input directory
  fili  = "output.bin"                    ; DSET
  fName = diri+fili                       ; path

  nlat  = 25                              ; YDEF
  mlon  = 49                              ; XDEF
  nlev  = 5                               ; LEV
  ntim  = 1                               ; REC
  vars  = 4                               ; VARS 
  UNDEF = 1.e30                           ; UNDEF

  ; create an array to contain data
  x     = new ( (/vars,nlev,nlat,mlon/), float, UNDEF)
  setfileoption("bin","ReadByteOrder","LittleEndian")
  do nt=0,ntim-1                          ; read each record: store in x
     x = fbindirread(fName, nt, (/vars,nlev,nlat,mlon/), "float")
  end do

  x!0 = "var"
  x!1 = "lev"
  x!2 = "lat"
  x!3 = "lon"
  x&lon= fspan(90.,180.,49)
  x&lat= fspan(15.,60.,25)
  x&lat@units="degrees_north"
  x&lon@units="degrees_east"

  h = x(0,:,:,:)
  h@long_name = "geopotential height"
  h@units     = "gpm"
  u = x(1,:,:,:)
  v = x(2,:,:,:)
  t = x(3,:,:,:)
  printVarSummary(h)
;-------------------------------------
  wks_type = "png"
  wks_type@wkWidth = 1000
  wks_type@wkHeight = 1000
  wks = gsn_open_wks(wks_type,"HW1")

  res           = True
  res@gsnAddCyclic = False
  res@mpFillOn = True                     ; turn on the map filling resource
  res@mpMinLonF = 90.
  res@mpMaxLonF = 180.
  res@mpMinLatF = 15.
  res@mpMaxLatF = 60.

  res@cnLevelSelectionMode = "ManualLevels"     ; manually set the contour levels with the following 3 resources
  res@cnMinLevelValF  = -200.                   ; set the minimum contour level
  res@cnMaxLevelValF  = 500.                    ; set the maximum contour level
  res@cnLevelSpacingF = 50.                     ; set the interval between contours
  plot = gsn_csm_contour_map(wks,h(0,:,:),res)

