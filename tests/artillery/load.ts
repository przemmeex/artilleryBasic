import { testDogPage, testCatPage } from '../commands/login';

export async function artilleryScript(page: any) {
    await testDogPage(page);
    await testCatPage(page);
}