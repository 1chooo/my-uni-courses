library ieee;

use IEEE.STD_LOGIC_1164.all;
use IEEE.STD_LOGIC_ARITH.all;
use IEEE.STD_LOGIC_UNSIGNED.all;

entity g0 is
port ( clk           : in  std_logic;
       rstn          : in  std_logic;
       en            : in  std_logic;
       L1            : in  std_logic;
       L2            : in  std_logic;
       V1            : out std_logic;
       V2            : out std_logic;
       M             : out std_logic;
       y0, y1, y2,y3 : out std_logic);
end g0;

architecture rtl of g0 is
    signal x0, x1, x2, x3 : std_logic;
    signal w_V1           : std_logic;
    signal w_v2           : std_logic;
    signal W_M            : std_logic;
begin
    GRAFECT: process (clk,rstn)
begin
    if rstn= '0' then
        x0 <= '1'; 
        x1 <= '0'; 
        x2 <= '0'; 
        x3 <= '0';
    elsif clk 'event and clk= '1' then
        if x0='1' and en='1' then
            x0 <= '0'; 
            x1 <= '1';
        elsif x1='1' and L1='1' then
            x1 <= '0'; 
            x2 <= '1'; 
            x3 <= '1';
        elsif x2='1' and x3='1' and L2='1' then
            x2 <= '0'; 
            x3 <= '0'; 
            x0 <= '1';
        else null;
        end if;
    else null;
    end if;
end process;

DATA_PATH : process (x0, x1,x2, x3)
    begin
        y0 <= x0; 
        y1 <= x1; 
        y2 <= x2; 
        y3 <= x3;
        if x0 = '1' then
            W_V1 <= '0'; 
            W_V2 <= '0'; 
            W_M <= '0';
        end if;
        if x1 = '1' then
            W_V1 <= '1';
        end if;
        if x2 = '1' then
            W_M <= '1';
        end if;
        if x3 = '1' then
            W_V2 <= '1';
        end if;
            V1 <= W_V1; 
            V2 <= W_V2; 
            M <= W_M;
    end process;
END rtl;