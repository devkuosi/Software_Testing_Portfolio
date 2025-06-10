export async function loginAsRole(page, role: 'admin' | 'manager' | 'contributor') {
    const users = {
        admin: { email: 'admin@taskforge.test', password: 'Test@123' },
        manager: { email: 'manager@taskforge.test', password: 'Test@123' },
        contributor: { email: 'user@taskforge.test', password: 'Test@123' }
    };

    const user = users[role];
    await page.goto('http://localhost/login');
    await page.fill('#email', user.email);
    await page.fill('#password', user.password);
    await page.click('button[type="submit"]');
    await page.waitForURL(/dashboard/);
}