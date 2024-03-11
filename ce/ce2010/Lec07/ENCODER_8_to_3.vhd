Library IEEE;
Use IEEE.std_logic_1164.all;

Entity Encoder_8_to_3 is
	Port(EN: in  std_logic;
		 A : in  std_logic_vector(7 downto 0);
		 Y : out std_logic_vector(2 downto 0));
End Encoder_8_to_3;

Architecture ARCH of Encoder_8_to_3 is
Begin
Process(EN, A)
Begin
	if(EN='1') and (A="10000000") then Y <= "111";
	elsif(EN='1') and (A="01000000") then Y <= "110";
	elsif(EN='1') and (A="00100000") then Y <= "101";
	elsif(EN='1') and (A="00010000") then Y <= "100";
	elsif(EN='1') and (A="00001000") then Y <= "011";
	elsif(EN='1') and (A="00000100") then Y <= "010";
	elsif(EN='1') and (A="00000010") then Y <= "001";
	else Y <= "000";

   End if;
End Process;
End ARCH;