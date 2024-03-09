# [AP3001] Atmospheric Dynamics

> AP3001 Atmospheric Dynamics
> 
> Year: 2023 Fall    
> Lecturer: 黃清勇

- $\zeta$: Vorticity (渦度)
- $\psi$: Stream function (流函數)

## 內重力(浮力)波 (InternalGravity(Buoyancy)Waves)

1. 內重力波恢復力是浮力
2. 氣塊往上跑是絕熱膨脹，會冷卻，往下就需要壓縮增溫（這時候比環境溫高，向上浮力）
3. 沒有重力是因為會跟氣壓梯度力平衡
4. 需要穩定的大氣，否則不會有內重力波產生

- $-N^{2}\delta{z}$: 浮力 (buoyancy) 
- $N$ static stability (靜力穩定度)
- $\nu = N\cos{\alpha}$ 頻率 (frequency) 跟 N 成正比以及 $\alpha$ 有關，水平方向震動頻率小，垂直方向震動頻率大

**布氏近似**
- 不可壓縮的大氣
- 排除聲波
- x, z 方向 (u, w)
- 位溫狀態方程
- 沒有 w bar 只有 w prime

The phase dispersion relationship (相位色散關係) of $\phi = kx + mz - vt$ for internal gravity waves is given by

- $\phi$: phase (相位)
- k and m: horizontal and vertical wavenumbers (水平和垂直波數)
- $\nu$: 隨時間變化的分量

## 輻散 v.s. 輻合

- 輻散 (divergence): $\nabla \cdot \vec{v} = \frac{\partial{u}}{\partial{x}} + \frac{\partial{v}}{\partial{y}} < 0$
- 輻合 (convergence): $\nabla \cdot \vec{v} = \frac{\partial{u}}{\partial{x}} + \frac{\partial{v}}{\partial{y}} > 0$

**解釋**
- 輻散: 風場 ($\vec{v}$) 從高壓區流向低壓區
- 輻合: 風場 ($\vec{v}$) 從低壓區流向高壓區
- 水平符合輻散: 風場 ($\vec{v}$) 從高度較高的地方流向低度較低的地方


## 地轉跟非地轉
- $\zeta_{g}$: Geostrophic vorticity (地轉渦度)
- $\zeta_{a}$: Ageostrophic vorticity (非地轉渦度) 
- $v_{g}$: Geostrophic wind (地轉風)
- $v_{a}$: Ageostrophic wind (非地轉風)
- 正渦度平流: $\zeta_{g} > 0$ 
- $\frac{\partial{\Phi}}{\partial{t}}$: 重力位 (geopotential)
- $\frac{\partial{\zeta_{g}}}{\partial{t}}$  (地轉渦度變化率)

## 抵銷
- 絕熱增溫可抵銷部分冷、暖平流作用

## 絕熱增溫 (adiabatic warming)

## 平流 (advection)
平流 (advection) 是指氣體隨著流體的移動而移動，而不是隨著流體的流動而移動。平流是一種物理過程，它是由於流體的流動而產生的。

- 冷平流 (cold advection): $v_{g} < 0$
- 暖平流 (warm advection): $v_{g} > 0$

### (5 marks) Briefly explain geostropic adjustion in relation to interia-gravity waves

中緯度大尺度大氣運動是接近地轉平衡的狀態，若離開此平衡，則會激發慣性重力波，趨於非地轉平衡，因此需要進行地轉調整來使質量場和動量場重新分配，以恢復地轉平衡。

**也就是因為激發慣性重力波，所以需要地轉調整來重新分配質量場和動量場，以恢復地轉平衡。**

```mermaid
graph LR;
    A[中緯度大尺度大氣運動是否接近地轉平衡?] -->|是| B[維持地轉平衡狀態]
    A -->|否| C[激發慣性重力波]
    C --> D[趨向非地轉平衡]
    D --> E[進行地轉調整]
    E --> F[重新分配質量場和動量場]
    F --> G[恢復地轉平衡]
```

### (5 marks) Describe the formation mechanism of free Rossby waves based on PV conservation.

- $\eta$: 絕對渦度
- $\zeta$: 渦度
- $f$: 科氏力參數表行星渦度

$\eta = \zeta + f$ 又 $\frac{\zeta + f}{h} = const.$

以北半球為例，討論氣塊向北以及向南的情況

- **向北:** $\zeta$ 增加，$f$ 減少，生成反氣旋環流，氣塊的西邊也為這個環流而有向北的速度分量，形成負的 $\zeta$，因此往北的氣塊西邊為負的 $\zeta$ 最強處，東側邊緣為向南運動，使氣塊往南。
- **向南:** $\zeta$ 減少，$f$ 增加，生成氣旋環流，氣塊的西邊也為這個環流而有向南的速度分量，形成正的 $\zeta$，因此往南的氣塊西邊為正的 $\zeta$ 最強處，東側邊緣為向北運動，使氣塊往北。

### (5 marks) Linearize the non-divergent barotropic vorticity equation expressed by the stream function $\psi'$ by assuming small perturbations with uniform zonal mean flow, 

### (5 marks) Derive the zonal phase speed of Rossby waves that will propagate upstream relative to the mean flow.

### (5 marks) Estimate the zonal phase speed of Rossby wave with $6,000 km$ wavelength relative to the mean flow.

### (5 marks) Estimate the zonal phase speed of Rossby wave with $10,000 km$ wavelength.

## 符號
[Basic-LaTeX-Commands](https://hackmd.io/@CynthiaChuang/Basic-LaTeX-Commands)
