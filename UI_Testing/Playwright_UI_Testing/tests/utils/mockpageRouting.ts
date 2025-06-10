import { mockLoginPage, mockDashboardPage } from './mockPages';
import { BrowserContext } from '@playwright/test';

/**
 * Sets up route mocking for Playwright tests to simulate backend responses
 * for the login and dashboard pages.
 *
 * - Intercepts requests to any URL ending with '/login' and responds with a static mock login page.
 * - Intercepts requests to any URL ending with '/dashboard' and responds with a mock dashboard page
 *   that displays the specified user role.
 *
 * @param context - The Playwright browser context in which to set up the mocks.
 * @param role - The user role to display on the mocked dashboard page.
 */
export async function mockPageRouting(context: BrowserContext, role: string) {
  // Mock the /login route to return the static login page HTML
  await context.route('**/login', async route => {
    await route.fulfill({
      contentType: 'text/html',
      body: mockLoginPage,
    });
  });

  // Mock the /dashboard route to return the dashboard page HTML with the correct role
  await context.route('**/dashboard', async route => {
    await route.fulfill({
      contentType: 'text/html',
      body: mockDashboardPage(role),
    });
  });
}       