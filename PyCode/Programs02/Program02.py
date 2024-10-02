def celsius_to_faranheit():
    temp = input("Enter a temperature in Celsius: ")
    temp = int(temp)

    temp_farahnheit = ((temp * 9) /5) + 32
    temp_farahnheit = str(temp_farahnheit)
    print("Your new temperature in fahranheit is: " + temp_farahnheit)

celsius_to_faranheit()