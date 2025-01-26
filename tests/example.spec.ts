import { expect, Page, test } from '@playwright/test';

import { testCatPage, testDogPage } from './commands/login';

test('test Dog Page', async ({ page }) => {
await testDogPage(page);
});

test('test Cat Page', async ({ page }) => {
    await testCatPage(page);
});
