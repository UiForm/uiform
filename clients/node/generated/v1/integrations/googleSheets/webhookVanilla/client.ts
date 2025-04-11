import { AbstractClient, CompositionClient, streamResponse } from '@/client';
import { WebhookRequest } from "@/types";

export default class APIWebhookVanilla extends CompositionClient {
  constructor(client: AbstractClient) {
    super(client);
  }


  async post({ spreadsheetId, organizationId, colorByLikelihood, appendLikelihoods, ...body }: { spreadsheetId: string, organizationId: string, colorByLikelihood?: boolean, appendLikelihoods?: boolean } & WebhookRequest): Promise<object> {
    let res = await this._fetch({
      url: `/v1/integrations/google_sheets/webhook_vanilla`,
      method: "POST",
      params: { "spreadsheet_id": spreadsheetId, "organization_id": organizationId, "color_by_likelihood": colorByLikelihood, "append_likelihoods": appendLikelihoods },
      body: body,
      bodyMime: "application/json",
    });
    if (res.headers.get("Content-Type") === "application/json") return res.json();
    throw new Error("Bad content type");
  }
  
}
