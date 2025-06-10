export const mockLoginPage = `
  <html>
    <body>
      <form id="login">
        <input id="email" placeholder="email" />
        <input id="password" type="password" />
        <button type="submit">Login</button>
      </form>
      <div id="result"></div>
      <script>
        document.getElementById('login').addEventListener('submit', function(e) {
          e.preventDefault();
          document.getElementById('result').innerText = 'Login successful';
          setTimeout(function() {
            window.location.href = '/dashboard';
          }, 100); // Simulate redirect after login
        });
      </script>
    </body>
  </html>
`;      

export function mockDashboardPage(role: string) {
  return `
    <html>
      <body>
        <h1 class="user-role">${role}</h1>
      </body>
    </html>
  `;
}
