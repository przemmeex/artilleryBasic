import { expect, test } from '@playwright/test';

import { testLogin } from './commands/login';

test('test', async ({ page }) => {
await testLogin(page);
});