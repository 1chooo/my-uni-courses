Library IEEE;
Use IEEE.std_logic_1164.all;

Entity DeMUX1_8 is
	Port( A : in  std_logic;
		  S : in  std_logic_vector(2 downto 0);
		  Y : out std_logic_vector(7 downto 0));
End DeMUX1_8;

Architecture ARCH of DeMUX1_8 is
Begin
	Y(0) <= A when S="000" else 'Z';
	Y(1) <= A when S="001" else 'Z';
	Y(2) <= A when S="010" else 'Z';
	Y(3) <= A when S="011" else 'Z';
	Y(4) <= A when S="100" else 'Z';
	Y(5) <= A when S="101" else 'Z';
	Y(6) <= A when S="110" else 'Z';
	Y(7) <= A when S="111" else 'Z';
End ARCH;
