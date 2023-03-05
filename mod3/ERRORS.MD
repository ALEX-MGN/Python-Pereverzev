
<table>
<tr>
       <td>
              НЕПРАВИЛЬНО
       </td>
       <td>
              ПРАВИЛЬНО
       </td>
<tr>
<tr>
       <td>
              def get_age(self):<br>
              &nbsp &nbsp now = datetime.datetime.now()<br>
              &nbsp &nbsp return self.yob - now.year
       </td>
       <td>
              def get_age(self):<br>
              &nbsp &nbsp now = datetime.datetime.now()<br>
              &nbsp &nbsp return now.year - self.yob
       </td>
</tr>
<tr>
       <td>
              def set_name(self, name): <br>
              &nbsp &nbsp self.name = self.name
       </td>
       <td>
              def set_name(self, name): <br>
              &nbsp &nbsp self.name = name
       </td>
</tr>
<tr>
       <td>
              def set_address(self, address): <br>
              &nbsp &nbsp self.address == address
       </td>
       <td>
              def set_address(self, address): <br>
              &nbsp &nbsp self.address = address
       </td>
</tr>
<tr>
       <td>
              def is_homeless(self): <br>
              &nbsp &nbsp return address is None
       </td>
       <td>
              def is_homeless(self): <br>
              &nbsp &nbsp return self.address is None
       </td>
</tr>
</table>