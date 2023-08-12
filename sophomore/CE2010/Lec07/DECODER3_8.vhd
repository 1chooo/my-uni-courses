LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;

ENTITY DECODER3_8 IS
	PORT( EN : IN STD_LOGIC;
			A  : IN  STD_LOGIC_VECTOR(2 DOWNTO 0);
			Y  : OUT STD_LOGIC_VECTOR(7 DOWNTO 0));
END DECODER3_8;

ARCHITECTURE ARCH OF DECODER3_8 IS
	SIGNAL TMP : TD_LOGIC_VECTOR(3 DOWNTO 0);
BEGIN
	WITH A SELECT
	Y <= "10000000" WHEN "111",
		  "01000000" WHEN "110",
		  "00100000" WHEN "101",
		  "00010000" WHEN "100",
		  "00001000" WHEN "011",
		  "00000100" WHEN "010",
		  "00000010" WHEN "001",
		  "00000001" WHEN "000";
END ARCH;