def get_date(new_data: str) ->str:
   user_data =  new_data[:10].split("-")[::-1]
   return f"{".".join(user_data)}"

print(get_date("2024-03-11T02:26:18.671407"))