import { test, expect } from '@playwright/test';
import { loginAsRole } from '../utils/roles';
import { mockPageRouting } from '../utils/mockpageRouting';

const roles = ['admin', 'manager', 'contributor'];

test.describe('RBAC Login Flow', () => {
  roles.forEach((role) => {
    test(`should log in as ${role}`, async ({ page, context }) => {
      await mockPageRouting(context, role);
      await loginAsRole(page, role);
      await expect(page).toHaveURL(/dashboard/);
      await expect(page.locator('.user-role')).toContainText(role);
    });
  });
});