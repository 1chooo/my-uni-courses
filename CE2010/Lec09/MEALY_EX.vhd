LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;

ENTITY MEALY_EX IS
	PORT( INPUT, CK : IN  STD_LOGIC;
		  PSTATE    : OUT INTEGER RANGE 0 TO 9; -- VIEW
		  OUTPUT    : OUT STD_LOGIC);
END MEALY_EX;

ARCHITECTURE FSM OF MEALY_EX IS
	TYPE STATES IS (S0, S1, S2, S3);
	SIGNAL PS : STATES := S0;
BEGIN
	PROCESS(CK)
		VARIABLE NS : STATES := S0;
	BEGIN
		IF RISING_EDGE(CK) THEN
		    CASE PS IS 
			    WHEN S0 =>
				    IF INPUT = '1' THEN
				        NS := S1;
					    PSTATE <= 1;
					    OUTPUT <= '0';
				    ELSE 
				        NS := S3;
					    PSTATE <= 3;
					    OUTPUT <= '0';
				    END IF;
			    WHEN S1 =>
			        IF INPUT = '1' THEN 
						NS := S2;
						PSTATE <= 2;
						OUTPUT <= '1';
					ELSE 
						NS := S1;
						PSTATE <= 1;
						OUTPUT <= '0';
					END IF;
				WHEN S2 =>
					IF INPUT = '1' THEN
						NS := S3;
						PSTATE <= 3;
						OUTPUT <= '0';
					ELSE 
					    NS := S1;
					    PSTATE <= 1;
						OUTPUT <= '0';
					END IF;
				WHEN S3 =>
					IF INPUT = '1' THEN
						NS := S0;
						PSTATE <= 0;
						OUTPUT <= '1';
					ELSE
					    NS := S1;
						PSTATE <= 3;
						OUTPUT <= '0';
					END IF;
				WHEN OTHERS => NULL;
			END CASE;
		END IF;
		PS <= NS;
	END PROCESS;
END FSM;