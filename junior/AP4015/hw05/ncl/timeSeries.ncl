function set_xy_marker_res(res: logical)
local local_res
begin
  local_res = res
  local_res@trYMaxF = 360.
  local_res@trYMinF = 0.
  local_res@xyMarkLineModes = "Markers"
  local_res@xyMarkers = 16        ; Markers style
  local_res@xyMarkerSizeF = 0.003
  local_res@xyMarkerColor = "navy" 
  local_res@vpHeightF = 0.4
  local_res@vpWidthF = 0.7
  return local_res
end



begin

data = readAsciiTable("../data/all_1601.obs", 11, "float", (/0, 0/))
; print(data)

; Catch the datas
WS = data(:, 4)
WD = data(:, 5)
Temperature = data(:, 6)
Pressure = data(:, 8)
RH = data(:, 7)
SR = data(:, 9)
xList = ispan(1, 1440*7, 1)

; *** Panel resource ***
resP = True                       ; modify the panel plot
; resP@gsnMaximize = True           ; use full 

; *** Basic resource ***
res = True
res@gsnDraw = False
res@gsnFrame = False
; tr: handle coordinate TRansformations
res@trXMaxF = 1440*7      ; Defines the upper bound of the X-Axis coordinate
res@trXMinF = 1           ; Defines the lower bound of the X-Axis coordinate
res@vpHeightF = 0.25
res@vpWidthF = 1.0
res@xyLineThicknesses = 5
; tmXB: TickMark X Bottom
res@tmXBMode = "Explicit"
res@tmXBValues = ispan(1, 1440*7, 1440)
res@tmXBLabels = (/"1/19", "1/20", "1/21", "1/22", "1/23", "1/24", "1/25"/)
res@tmYLLabelFontHeightF = 0.0075
res@tmXBLabelFontHeightF = 0.015   ; set the bottom X-axis tick mark label font size


wks_type = "png"
wks_type@wkWidth = 5000  ; increase this size for better resolution
wks_type@wkHeight = 4000 ; increase this size for better resolution
wks_1 = gsn_open_wks(wks_type, "../image/Fig_week")


; -----  Picture 1: Temperature and Relative Humidity  ----- ;
Temperature_res = res
RH_res = res
Temperature_res@xyLineColors = "maroon2"
RH_res@xyLineColors = "springgreen4"

plotTemperature_and_RH = gsn_csm_xy2(wks_1, xList, Temperature, RH, Temperature_res, RH_res)

; -----  Picture 2: Solar Radiation and Pressure  ----- ;
SR_res = res
Pressure_res = res
SR_res@xyLineColors = "red"
SR_res@gsnYRefLine = 0.0     ; create a reference line
SR_res@gsnAboveYRefLineColor = "violetred1"

plotSR_and_Pressure = gsn_csm_xy2(wks_1, xList, SR, Pressure, SR_res, Pressure_res)

; -----  Picture 3: Wind Speed and Wind Direction  ----- ;
WS_res = res
WD_res = set_xy_marker_res(res)
WS_res@xyLineColors = "goldenrod1"

plotWS_and_WD = gsn_csm_xy2(wks_1, xList, WS, WD, WS_res, WD_res)

; Put pictures into a panel
gsn_panel(wks_1, (/plotTemperature_and_RH, plotSR_and_Pressure, plotWS_and_WD/), (/3, 1/), resP)


wks_2 = gsn_open_wks(wks_type, "../image/Fig_day0119")
res@trXMaxF = 1440*5+1439      ; Defines the upper bound of the X-Axis coordinate
res@trXMinF = 1440*5
res@tmXBValues := ispan(0, 1439, 60)
res@tmXBLabels := ispan(0, 23, 1)

; -----  Picture 1: Temperature and Relative Humidity  ----- ;
Temperature_res = res
RH_res = res
Temperature_res@xyLineColors = "maroon2"
RH_res@xyLineColors = "springgreen4"

plotTemperature_and_RH = gsn_csm_xy2(wks_2, xList(1440*5:1440*5+1439), Temperature(1440*5:1440*5+1439), RH(1440*5:1440*5+1439), Temperature_res, RH_res)

; -----  Picture 2: Solar Radiation and Pressure  ----- ;
SR_res = res
Pressure_res = res
SR_res@xyLineColors = "red"
SR_res@gsnYRefLine = 0.0     ; create a reference line
SR_res@gsnAboveYRefLineColor = "violetred1"

plotSR_and_Pressure = gsn_csm_xy2(wks_2, xList(1440*5:1440*5+1439), SR(1440*5:1440*5+1439), Pressure(1440*5:1440*5+1439), SR_res, Pressure_res)

; -----  Picture 3: Wind Speed and Wind Direction  ----- ;
WS_res = res
WD_res = set_xy_marker_res(res)
WS_res@xyLineColors = "goldenrod1"

plotWS_and_WD = gsn_csm_xy2(wks_2, xList(1440*5:1440*5+1439), WS(1440*5:1440*5+1439), WD(1440*5:1440*5+1439), WS_res, WD_res)

; Put pictures into a panel
gsn_panel(wks_2, (/plotTemperature_and_RH, plotSR_and_Pressure, plotWS_and_WD/), (/3, 1/), resP)


wks_3 = gsn_open_wks(wks_type, "../image/Fig_average")
Average_res = res
delete(Average_res@trXMaxF)
delete(Average_res@trXMinF)
Average_res@tmXBValues := (/0, 1, 2, 3, 4, 5, 6/)
Average_res@tmXBLabels := (/"1/19", "1/20", "1/21", "1/22", "1/23", "1/24", "1/25"/)
Average_blue_res = Average_res
Average_blue_res@xyLineColors = "blue"


TemperatureAvg = new(7, float)
PressureAvg = new(7, float)
do day = 0, 6
    TemperatureAvg(day) = dim_avg(Temperature(1440*day:1440*day+1439))
    PressureAvg(day) = dim_avg(Pressure(1440*day:1440*day+1439))
end do

plotAverage = gsn_csm_xy2(wks_3, (/0, 1, 2, 3, 4, 5, 6/), TemperatureAvg, PressureAvg, Average_res, Average_blue_res)
gsn_panel(wks_3, (/plotAverage/), (/1, 1/), resP)


end
