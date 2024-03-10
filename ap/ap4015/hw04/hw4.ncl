; Functions definition ---------------------
function set_maps_res(res: logical)
local local_res
begin
  local_res = res

  local_res@mpLimitMode     = "LatLon"       ; required
  local_res@mpMinLatF       =  15.           ; min lat
  local_res@mpMaxLatF       =  60.           ; max lat
  local_res@mpMinLonF       =  90.           ; min lon
  local_res@mpMaxLonF       = 180.           ; max lon
  
  return local_res
end

function set_isotherm_contour_res(res: logical)
local local_res
begin
  local_res = res

  local_res@gsnAddCyclic     = False
  
  local_res@cnFillOn         = True       ; areas between contour levels are filled with a solid color
  local_res@cnLinesOn        = False      ; turn off contour lines
  ;local_res@cnLineLabelsOn  = False      ; tuen off line labels
  local_res@lbLabelBarOn     = True       ; will draw a panel label bar
  return local_res
end

function set_isobaric_contour_res(res: logical)
local local_res
begin
  local_res = res

  local_res@gsnAddCyclic     = False

  local_res@cnLevelSpacingF  = 5
  local_res@tiMainOn         = False         ; turns the Main title off.
  ; local_res@cnFillPalette    = "gui_default" ; set color map
  local_res@cnLineLabelBackgroundColor = -1
  local_res@cnInfoLabelOn    = False         ; Robin ask: what is this?
  local_res@lbLabelBarOn     = False         ; will draw a panel label bar instead
  local_res@cnLineColor      = "white"
  local_res@cnLineThicknessF = 3.0
  
  return local_res
end

function set_windbar_vector(res: logical)
local local_res
begin
  local_res = res

  local_res@gsnAddCyclic             = False

  local_res@vcGlyphStyle             = "WindBarb"     ; select wind barbs
  local_res@vcRefLengthF             = 0.008          ; define length of vec ref
  local_res@vcRefAnnoOn              = False          ; turn off ref wind barb
  local_res@vcMinDistanceF           = 0.012          ; thin out windbarbs
  local_res@vcWindBarbLineThicknessF = 3.             ; set the wind barb thickness
  local_res@trYReverse               = True           ; reverse the Y-axis
  local_res@vcWindBarbColor          = (/111, 111, 111/) / 255.

  return local_res
end

function set_isotach_contour_res(res: logical)
local local_res
begin
  local_res = res
  local_res@gsnAddCyclic     = False

  local_res@cnFillOn         = False
  local_res@cnInfoLabelOn    = False         ; Robin ask: what is this?
  local_res@cnMonoLineColor  = False         ; control the color of each line individually
  local_res@cnLineColors     = span_color_rgba("NCV_jet",15)   ; 256 colors, span it to get 11 colors
  local_res@cnLineThicknessF = 3.0
  return local_res
end


; Main program strat -----------------------
begin
path = "/Users/robinhsieh/Programming/NCL/meteorology/HW4/"

; If -1 is given for the dimensions parameter,
; all values in the file will be read into a one-dimensional variable.
lines  = asciiread(path+"012400.txt", -1, "string")

; The dimension size of this variable will be equal to the number of elements in the file.
nlines = dimsizes(lines)

;;print(nlines)
;;print(lines)

mlon  = 121 ; range: 90~180, step: 0.75
nlat  = 61  ; range: 15~60, step: 0.75
levs  = 5   ; 300, 500, 700, 850, 1000
vars  = 4   ; H, U, V, T

; 'var': Processing the data in 'lines', store 4-dimension data about:
; vars=0: values of Geopotential meters height (H), unit: GPM, in latitude and longitude grid
; vars=1: values of Meridional wind speed (U), in latitude and longitude grid
; vars=2: values of Zonal wind speed (V), in latitude and longitude grid
; vars=3: values of Temperature (T), unit: Kelvin, in latitude and longitude grid
var = new((/vars, levs, nlat, mlon/), float)

pressure_levels = (/300, 500, 700, 850, 1000/)

nl   = 0    ; Count line
nvar = 0    ; Record data types in (H=0, U=1, V=2, T=3)
nlev = 0    ; Record isobaric surfaces in (300hPa=0, 500hPa=1, 700hPa=2, 850hPa=3, 1000hPa-4)
do while(nl .lt. nlines)
;---Read the first character of this line, return substring: (string, start, end)
  first = str_get_cols(lines(nl), 0, 0)
;---If it's a "%", then increment to next line.
  if(first .eq. "D") then
    nl = nl + 1           ; increment line counter, skip 'DATE=160124  HOUR=00  PLEVEL= ...'
    continue
  else
;---Otherwise, get the number of rows and read the data.
    
    ; In 012400.txt, every 739 lines contains a complete set of data
    ; of latitude and longitude grid, (121*61 = 739*10-1 = 7381 values).
    nrows = 739
    
    if(nvar .gt. vars-1)then
       nvar = 0           ; reset the type of variable to Geopotential meters height (H)
       nlev = nlev + 1    ; switch to different isobaric surface, ex: 300, 500, 700, 850, 1000
    end if
    nl = nl + 1           ; increment line counter, skip '**** ...  ****'
    ;;print("==================================================")
    ;;print("Reading " + nrows + " rows of data.")

    ; Clean up the strings so there's only one space between each string,
    ; and no extra space at beginning or end.
    ; This allows us to use str_split_csv to parse this chunk of data.
    ; str_split_csv expects a single character delimiter (a space in this case).
    lines(nl:nl+nrows-1) = str_sub_str(lines(nl:nl+nrows-1),"    "," ")
    lines(nl:nl+nrows-1) = str_sub_str(lines(nl:nl+nrows-1),"   "," ")
    lines(nl:nl+nrows-1) = str_sub_str(lines(nl:nl+nrows-1),"  "," ")
    
    ; Returns an array of strings with leading and ending spaces and TABs removed.
    lines(nl:nl+nrows-1) = str_strip(lines(nl:nl+nrows-1))

    ; Parse the data into a 2D integer array.
    x2D = tofloat(str_split_csv(lines(nl:nl+nrows-1), " ", 0))

    ; Converts a multi-dimensional array to a one-dimensional array.
    x1D =  ndtooned(x2D)
    ;;print(x1D(0:121*61-1))
    ;;print(nvar+" "+nlev)
    
    ; Reshapes a multi-dimensional array to another multi-dimensional array.
    var(nvar, nlev, :, :) = reshape(x1D(0:mlon*nlat-1), (/nlat, mlon/))
    ;;print(x1D(0)+"  "+x1D(mlon*nlat-1))   
    
    nl = nl + nrows     ; Jump to next set of data (latitude and longitude grid).
    nvar = nvar + 1     ; switch to different types of variable, ex: H, U, V, T
  end if
end do

lat_coor = fspan(15, 60, nlat)
lon_coor = fspan(90, 180, mlon)

H = var(0, :, :, :) ; Geopotential meters height
H!0 = "lev"
H!1 = "lat"
H!2 = "lon"
H&lat = lat_coor
H&lon = lon_coor
H&lat@units = "degrees_north"
H&lon@units = "degrees_east"

U = var(1, :, :, :) ; Meridional wind speed
V = var(2, :, :, :) ; Zonal wind speed
T = var(3, :, :, :) ; Temperature

; Copies all named dimensions and coordinate variables from one variable to another.
copy_VarCoords(H, U)
copy_VarCoords(H, V)
copy_VarCoords(H, T)

res                   = True           ; plot mods desired
res@gsnDraw           = False          ; don't draw graphics when the gsn function is called
res@gsnFrame          = False          ; don't advance frame when the gsn function is called

do level = 0, levs-1
  wks = gsn_open_wks("png", "hw4_total_"+pressure_levels(level)+"hPa")  ; send graphics to PNG file

  map_res = set_maps_res(res)
  map_res@tiMainString = pressure_levels(level) + "hPa Temperature, height and wind field" ; add titles
  ; map = gsn_csm_map(wks, map_res)

  temperature_res = set_isotherm_contour_res(map_res)
  ; temperature_res = set_isotherm_contour_res(res)

  ;print(temperature_res)
  ; isotherm_contour = gsn_csm_contour(wks, T(level, :, :), temperature_res)
  isotherm_contour = gsn_csm_contour_map(wks, T(level, :, :), temperature_res)

  gpm_res = set_isobaric_contour_res(res)
  gpm_res@cnFillOn                = False
  ;gpm_res@cnLineLabelPerimOn     = False
  if (pressure_levels(level) .le. 500)then
    gpm_res@cnLevelSpacingF = 60
  else
    gpm_res@cnLevelSpacingF = 30
  end if
  ;print(gpm_res)
  isobaric_contour = gsn_csm_contour(wks, H(level, :, :), gpm_res)

  vector_res = set_windbar_vector(res)
  ;print(vector_res)
  windbars = gsn_csm_vector(wks, U(level, :, :), V(level, :, :), vector_res)
  
  ; overlay(map, isotherm_contour)
  ; overlay(map, isobaric_contour)
  overlay(isotherm_contour, isobaric_contour)
  overlay(isotherm_contour, windbars)
  ; overlay(map, windbars)
  ; draw(map)
  draw(isotherm_contour)
  frame(wks)
end do

do level = 0, levs-1
  wks = gsn_open_wks("png", "hw4_streamline_"+pressure_levels(level)+"hPa")
  map_res@tiMainString = pressure_levels(level) + "hPa Streamline" ; add titles
  map_res = set_maps_res(res)

  map = gsn_csm_map(wks, map_res)

  stream_line = gsn_csm_streamline(wks, U(level, :, :), V(level, :, :), res)
  
  overlay(map, stream_line)
  draw(map)
  frame(wks)
end do

Wind_speed_scalar = new((/levs, nlat, mlon/), float)
; Calculate wind speed scalar
do level = 0, levs-1
  do lat = 0, nlat-1
    do lon = 0, mlon-1
      Wind_speed_scalar(level, lat, lon) = (U(level, lat, lon)^2 + V(level, lat, lon)^2)^0.5
    end do
  end do
end do
copy_VarCoords(H, Wind_speed_scalar)

do level = 0, levs-1
  wks = gsn_open_wks("png", "hw4_isotach_contour"+pressure_levels(level)+"hPa")
  map_res = set_maps_res(res)
  map_res@tiMainString = pressure_levels(level) + "hPa Isotach line" ; add titles
  map = gsn_csm_map(wks, map_res)

  windspeed_res = set_isotach_contour_res(res)
  isotach_contour = gsn_csm_contour(wks, Wind_speed_scalar(level, :, :), windspeed_res)

  overlay(map, isotach_contour)
  draw(map)
  frame(wks)
end do

end

