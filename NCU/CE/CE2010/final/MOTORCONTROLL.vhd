LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;
USE IEEE.STD_LOGIC_ARITH.ALL;
USE IEEE.STD_LOGIC_UNSIGNED.ALL;


ENTITY MOTORCONTROLL IS
	PORT(
		START, DIR, CLK, RST : IN  STD_LOGIC;
		S3, S2, S1, S0       : OUT STD_LOGIC
		);
END MOTORCONTROLL;


ARCHITECTURE ARCH OF MOTORCONTROLL IS
	SIGNAL X0, X1, X2, X3 : STD_LOGIC;
	SIGNAL A0, A1, A2, A3 : STD_LOGIC;
	
BEGIN

GRAFCET : PROCESS( CLK, RST)
BEGIN
	IF RST = '0' THEN
		X0 <= '1';
		X1 <= '0';
		X2 <= '0';
		X3 <= '0';
	ELSIF CLK'EVENT AND CLK = '1' THEN
		IF X0 = '1' AND START = '1' THEN
			X0 <= '0';
			X1 <= '1';
		ELSIF X1 = '1' AND DIR = '1' THEN
			X1 <= '0';
			X2 <= '1';
		ELSIF X1 = '1' AND DIR = '0' THEN
			X1 <= '0';
			X3 <= '1';
		ELSIF X2 = '1' AND DIR = '0' THEN
			X2 <= '0';
			X3 <= '1';
		ELSIF X3 = '1' AND DIR = '1' THEN
			X3 <= '0';
			X2 <= '1';
		ELSE NULL;
		END IF;
	ELSE NULL;
	END IF;
END PROCESS;


DATA_PATH : PROCESS(X0, X1, X2, X3)
	BEGIN
		IF CLK'EVENT AND CLK = '1' THEN
			IF X0 = '1' THEN
				A3 <= '1';
				A2 <= '1';
				A1 <= '0';
				A0 <= '0';
			ELSIF X2 = '1' THEN
				IF A3 = '1' AND A2 = '1' THEN
					A3 <= '0';
					A2 <= '1';
					A1 <= '1';
					A0 <= '0';
				ELSIF A2 = '1' AND A1 = '1' THEN
					A3 <= '0';
					A2 <= '0';
					A1 <= '1';
					A0 <= '1';
				ELSIF A1 = '1' AND A0 = '1' THEN
					A3 <= '1';
					A2 <= '0';
					A1 <= '0';
					A0 <= '1';
				ELSIF A3 = '1' AND A0 = '1' THEN
					A3 <= '1';
					A2 <= '0';
					A1 <= '1';
					A0 <= '0';
				ELSIF A3 = '1' AND A1 = '1' THEN
					A3 <= '0';
					A2 <= '1';
					A1 <= '0';
					A0 <= '1';
				ELSIF A2 = '1' AND A0 = '1' THEN
					A3 <= '1';
					A2 <= '1';
					A1 <= '0';
					A0 <= '0';
				END IF;
			ELSIF X3 = '1' THEN
				IF A3 = '1' AND A2 = '1' THEN
					A3 <= '0';
					A2 <= '1';
					A1 <= '0';
					A0 <= '1';
				ELSIF A2 = '1' AND A0 = '1' THEN
					A3 <= '1';
					A2 <= '0';
					A1 <= '1';
					A0 <= '0';
				ELSIF A3 = '1' AND A1 = '1' THEN
					A3 <= '1';
					A2 <= '0';
					A1 <= '0';
					A0 <= '1';
				ELSIF A3 = '1' AND A0 = '1' THEN
					A3 <= '0';
					A2 <= '0';
					A1 <= '1';
					A0 <= '1';
				ELSIF A1 = '1' AND A0 = '1' THEN
					A3 <= '0';
					A2 <= '1';
					A1 <= '1';
					A0 <= '0';
				ELSIF A2 = '1' AND A1 = '1' THEN
					A3 <= '1';
					A2 <= '1';
					A1 <= '0';
					A0 <= '0';
				END IF;
			END IF;
			S3 <= A3;
			S2 <= A2;
			S1 <= A1;
			S0 <= A0;
		END IF;
	END PROCESS;
END ARCH;
