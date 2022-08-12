LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;
USE IEEE.STD_LOGIC_ARITH.ALL;
USE IEEE.STD_LOGIC_UNSIGNED.ALL;

ENTITY MULTIPLIER3BY3 IS
	PORT(
		A, B : IN  STD_LOGIC_VECTOR( 2 DOWNTO 0 );
		P    : OUT STD_LOGIC_VECTOR( 5 DOWNTO 0 )
		);
END MULTIPLIER3BY3;


ARCHITECTURE ARCH OF MULTIPLIER3BY3 IS
	CONSTANT N : INTEGER := 3;
	SUBTYPE PART IS STD_LOGIC_VECTOR( N - 1 DOWNTO 0 );
	TYPE PARTS IS ARRAY( 0 TO 4 ) OF PART;
	SIGNAL PP, PC, PS : PARTS;
	
BEGIN
	PGEN : FOR J IN 0 TO N - 1 GENERATE
		PGEN : FOR K IN 0 TO N - 1 GENERATE
			PP( J ) ( K ) <= A( K ) AND B( J );
		END GENERATE;
	END GENERATE;
	
	PP(4)(2) <= '0';
	PP(4)(1) <= '0';
	PP(4)(0) <= '0';
	PS(0) <= PP(0);
	P(0)  <= PP(0)(0);
	
	ADDR : FOR J IN 1 TO N - 1 GENERATE
		ADDC : FOR K IN 0 TO N - 2 GENERATE
			PS(J)(K) <= PP(J)(K) XOR 
							PC(J - 1)(K) XOR 
							PS(J - 1)(K + 1);
			PC(J)(K) <= (PP(J)(K) AND PC(J - 1)(K)) OR 
							(PP(J)(K) AND PS(J - 1)(K + 1)) OR 
							(PC(J-1)(K) AND PS(J-1)(K+1));
		END GENERATE;
		P(J) <= PS(J)(0);
		PS(J)(N - 1) <= PP(J)(N - 1);
	END GENERATE;
	
	PC(1)(2) <= '0';
	PC(2)(2) <= '0';
	PS(4)(0) <= '0';
	PC(N)(0) <= '0';
	
	ADDLAST : FOR K IN 1 TO N - 1 GENERATE
		PS(N)(K) <= PC(N)(K-1) XOR 
						PC(N - 1)(K - 1) XOR 
						PS(N - 1)(K);
		PC(N)(K) <= (PC(N)(K - 1) AND PC(N -1)(K - 1)) OR 
						(PC(N)(K - 1) AND PS(N - 1)(K)) OR 
						(PC(N - 1)(K - 1) AND PS(N - 1)(K));
	END GENERATE;
	
	P( 2 * N - 1) <= PC(N)(N - 1);
	P( 2 * N - 2 DOWNTO N ) <= PS(N)(N - 1 DOWNTO 1);
END ARCH;