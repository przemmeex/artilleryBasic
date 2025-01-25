import { expect } from '@playwright/test';

export async function testLogin(page: any) {
    await page.goto('https://en.wikipedia.org/wiki/Dog');
    await page.getByRole('link', { name: 'dingoes', exact: true }).click();
    await expect(page.getByRole('heading', { name: 'Dingo', exact: true }).locator('span')).toBeVisible();
}